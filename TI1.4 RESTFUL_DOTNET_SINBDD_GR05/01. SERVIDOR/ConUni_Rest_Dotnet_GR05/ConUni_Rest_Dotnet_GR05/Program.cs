var builder = WebApplication.CreateBuilder(args);

// Configurar para escuchar en todas las interfaces (0.0.0.0)
builder.WebHost.UseUrls("http://0.0.0.0:5000");

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring OpenAPI at https://aka.ms/aspnet/openapi
builder.Services.AddOpenApi();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

// Comentado para desarrollo solo con HTTP
// app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
