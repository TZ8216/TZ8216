import numpy as np
from scipy.integrate import dblquad

# 定义磁场 B = (y, x, z)
def B_field(x, y, z):
    return np.array([y, x, z])

# 圆柱参数化 (θ, z) → (2cosθ, 2sinθ, z)
def cylindrical_surface(theta, z):
    R = 2  # 半径
    x = R * np.cos(theta)
    y = R * np.sin(theta)
    return x, y, z

# 计算 dS = (∂r/∂θ × ∂r/∂z) dθ dz
def dS(theta, z):
    d_r_theta = np.array([-2 * np.sin(theta), 2 * np.cos(theta), 0])  # ∂r/∂θ
    d_r_z = np.array([0, 0, 1])  # ∂r/∂z
    cross = np.cross(d_r_theta, d_r_z)  # 叉积
    return cross

# 计算 B·dS
def integrand(theta, z):
    x, y, z = cylindrical_surface(theta, z)
    B = B_field(x, y, z)
    dS_vec = dS(theta, z)
    return np.dot(B, dS_vec)

# 计算曲面积分 ∫∫ B·dS (θ∈[0,2π], z∈[0,3])
flux, error = dblquad(integrand, 0, 3, lambda z: 0, lambda z: 2 * np.pi)
print(f"磁通量 Φ_B = {flux} (理论值应为 0)")