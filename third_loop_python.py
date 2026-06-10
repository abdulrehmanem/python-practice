# leds = []
# for LED in range(5):
#     leds.append(f'led{LED}')

# print(leds)

# leds = (f'L{led}' for led in range(1,11))
# print(list(leds))

# leds = list(f'L{led}' for led in range(1,16))
# print(leds)

leds = [f'L{led}' for led in range(1,6)]
# print(leds)
print(max(leds))
print(min(leds))

led_s = [led**2 for led in range(1,6)]
print(f'{led_s} Sum of squares = {sum(led_s)}')
