pip install pygame

To see an example of pygame, run the following command in terminal:
python3 -m pygame.examples.aliens

## Coordinate systems on windows:
- Top left starts from 0 and numbers increase as we go right and down.

## Creating colors
We create colors using RGB.
```python
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_GRAY = (175, 175, 175)
```

## While loop vs event-driven models
Event drivwn models dont rely on `input()` and `print()`, instaed they rely on the users interaction with the window.
