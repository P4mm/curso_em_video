import math

angle = float(input("Digite o ângulo em graus: "))

# Convert angle to radians
angle_rad = math.radians(angle)

# Calculate sine, cosine, and tangent
sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)

# Display the results
print(f"Seno: {sin_value:.2f}")
print(f"Cosseno: {cos_value:.2f}")
print(f"Tangente: {tan_value:.2f}")
