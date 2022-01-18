using IOT_Backend.Models;
using Microsoft.EntityFrameworkCore;

namespace IOT_Backend.Data
{
    public class ParkingRowDbContext : DbContext
    {

        public DbSet<ParkingRow> ParkingRows { get; set; }

        public ParkingRowDbContext(DbContextOptions<ParkingRowDbContext> options) : base(options)
        {

        }
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer(
                @"Server=(localDb)\IOT;Database=MasterProjekt_IOT;Integrated Security=True");
        }
    }
}
