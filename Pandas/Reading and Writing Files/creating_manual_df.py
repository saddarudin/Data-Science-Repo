import pandas as pd

df = pd.DataFrame(
    {
        'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'temperature': [17, 18, 21, 16, 18, 19, 22],
        'weather': ['sunny', 'hot', 'cloudy', 'raining', 'hot', 'sunny', 'cloudy']
    }
)

print(df)
