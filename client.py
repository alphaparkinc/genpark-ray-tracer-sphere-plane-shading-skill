"""3D Ray Tracing & Geometric Intersection Engine
100% Python Standard Library (math).
"""

import math

class Ray3D:
    """Normalized 3D Ray."""
    def __init__(self, origin, direction):
        self.origin = origin
        mag = math.hypot(direction[0], direction[1], direction[2])
        self.direction = [d / mag for d in direction]

class RayTracerEngine:
    """Geometric ray caster with Phong reflection shading."""
    def intersect_sphere(self, ray, center, radius):
        oc = [ray.origin[i] - center[i] for i in range(3)]
        a = sum(d * d for d in ray.direction)
        b = 2.0 * sum(oc[i] * ray.direction[i] for i in range(3))
        c = sum(oc[i] * oc[i] for i in range(3)) - radius * radius
        discriminant = b * b - 4.0 * a * c

        if discriminant < 0:
            return None
        t = (-b - math.sqrt(discriminant)) / (2.0 * a)
        return round(t, 4) if t > 0 else None

    def shade(self, hit_point, normal, light_pos):
        l_dir = [light_pos[i] - hit_point[i] for i in range(3)]
        l_mag = math.hypot(*l_dir)
        l_norm = [d / l_mag for d in l_dir]
        diff = max(0.0, sum(normal[i] * l_norm[i] for i in range(3)))
        intensity = 0.1 + 0.9 * diff
        return round(intensity, 4)
