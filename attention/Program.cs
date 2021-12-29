using attention.src.shared.infrastructure;
using attention.src.shared.domain;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddSingleton<EventBusConnection, RabbitMqConnection>();
builder.Services.AddTransient<EventBus, RabbitMqEventBus>();
builder.Services.AddDomainEventInformation();
builder.Services.AddTransient<EventBusConfiguration, RabbitMqEventBusConfiguration>();
builder.Services.AddTransient<DomainEventJsonDeserializer, DomainEventJsonDeserializer>();
builder.Services.AddTransient<DomainEventConsumer, RabbitMqDomainEventConsumer>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseAuthorization();

app.MapControllers();

// Configure rabbitMQ
var eventBus = app.Services.GetRequiredService<EventBusConfiguration>();
eventBus.configure();

var eventConsumer = app.Services.GetRequiredService<DomainEventConsumer>();
eventConsumer.consume();

app.Run();