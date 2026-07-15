import numpy as np

from cartesian_plane import draw

# {(x,y) ∈ R² : x²+y² ≤ 1} × [0,1]
# A × B has a constant cross-section A at every level of B, so this is a
# solid unit cylinder: the closed unit disk at every height z ∈ [0,1].
def plot(plt, ax):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    theta = np.linspace(0, 2 * np.pi, 100)

    # Lateral surface: r = 1, θ ∈ [0,2π], z ∈ [0,1]
    z = np.linspace(0, 1, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x = np.cos(theta_grid)
    y = np.sin(theta_grid)
    ax.plot_surface(x, y, z_grid, rstride=4, cstride=4, color='gray')

    # Filled disks r ∈ [0,1], θ ∈ [0,2π] capping the cylinder at z = 0 and z = 1
    r = np.linspace(0, 1, 50)
    r_grid, theta_cap = np.meshgrid(r, theta)
    x_cap = r_grid * np.cos(theta_cap)
    y_cap = r_grid * np.sin(theta_cap)
    ax.plot_surface(x_cap, y_cap, np.zeros_like(x_cap), color='gray')
    ax.plot_surface(x_cap, y_cap, np.ones_like(x_cap), color='gray')

    # Keep radius-1, height-1 proportions honest (x:y:z spans of 2:2:1)
    ax.set_box_aspect((1, 1, 0.5))
draw(plot)
