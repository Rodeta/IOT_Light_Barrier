using IOT_Backend.Data;
using IOT_Backend.Models;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace IOT_Backend.Controller
{
    [EnableCors("CorsApi")]
    [Route("api/parkingrow")]
    [ApiController]
    public class ParkingRowController : ControllerBase
    {
        private readonly ParkingRowDbContext _context;
        private readonly ILogger<ParkingRowController> _logger;

        /// <summary>
        /// Initialize Controller.
        /// </summary>
        /// <param name="context"> Database context</param>
        /// <param name="logger"> Logging parameter</param>
        public ParkingRowController(ParkingRowDbContext context, ILogger<ParkingRowController> logger)
        {
            _context = context;
            _logger = logger;
        }

        [HttpGet]
        public async Task<IActionResult> GetAllParkingRows()
        {
            return Ok(await _context.ParkingRows.ToListAsync());
        }

        /// <summary>
        /// 
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        [HttpGet("{id}")]
        public async ValueTask<IActionResult> GetParkingRow(int id)
        {
            var row = await _context.ParkingRows.Where(i => i.Id == id).FirstOrDefaultAsync();
            if (row is null)
            {
                return NotFound();
            }
            else
            {
                return Ok(row);
            }
        }

        [HttpPatch("{parkingRowId:int}")]
        public async ValueTask<IActionResult> UpdateFreeSpace([FromRoute] int parkingRowId, [FromBody] ParkingRowDto dto)
        {
            var row = await _context.ParkingRows.Where(pr => pr.Id == parkingRowId).FirstOrDefaultAsync();
            if(row is null)
            {
                return NotFound($"Parking row with id {parkingRowId} is not found.");
            }
            else
            {
                if (dto.Increasing)
                {
                    if (row.FreeSpace == row.MaxSpace) return Conflict($"Can not increase above max space of {row.MaxSpace}.");
                    row.FreeSpace++;
                    await _context.SaveChangesAsync();
                    return Ok($"Free space at parking row with id {parkingRowId} was increased");
                }
                else
                {
                    if (row.FreeSpace == 0) return Conflict($"Can not decrease below 0.");
                    row.FreeSpace--;
                    await _context.SaveChangesAsync();
                    return Ok($"Free space at parking row with id {parkingRowId} was decreased.");
                }
            }
        }       
    }
}
