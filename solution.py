import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import t


chat_id = 1444511418 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    alpha = 1 - p
    t_alpha_2 = t.ppf(1 - alpha / 2, n - 1)
    lower = loc - t_alpha_2 * scale
    upper = loc + t_alpha_2 * scale
    return (lower, upper)
