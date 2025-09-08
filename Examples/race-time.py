# You run a 10-kilometer race in 43 minutes 30 seconds.
# 1. What is your average time per mile (in minutes and seconds)?
# 2. What is your average speed in miles per hour?

# Hint: 1 mile = 1.61 kilometers.

# -----------------------------
# Race details
# -----------------------------
distance_km = 10  # kilometers
minutes = 43
seconds = 30

# Convert total time to minutes
total_time_min = minutes + seconds / 60  # 43 + 30/60 = 43.5 minutes

# -----------------------------
# Average speed in km/h
# -----------------------------
time_hours = total_time_min / 60  # Convert minutes to hours
speed_kmh = distance_km / time_hours
print(f"Average speed: {speed_kmh:.2f} km/h")

# -----------------------------
# Convert speed to miles per hour
# -----------------------------
distance_miles = distance_km / 1.61
speed_mph = distance_miles / time_hours
print(f"Average speed: {speed_mph:.2f} mph")

# -----------------------------
# Average time per mile
# -----------------------------
avg_time_per_mile_min = 60 / speed_mph  # minutes per mile
avg_minutes = int(avg_time_per_mile_min)
avg_seconds = (avg_time_per_mile_min - avg_minutes) * 60
print(f"Average time per mile: {avg_minutes} minutes {avg_seconds:.0f} seconds")
