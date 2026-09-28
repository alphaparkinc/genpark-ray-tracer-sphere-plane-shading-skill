from client import RayTracerEngine, Ray3D

def main():
    rt = RayTracerEngine()
    ray = Ray3D([0, 0, -5], [0, 0, 1])
    hit = rt.intersect_sphere(ray, [0, 0, 0], 1.0)
    print("Ray Tracer Engine Verification:")
    print(f"Intersection Distance: {hit} (Expected: 4.0)")
    intensity = rt.shade([0, 0, -1], [0, 0, -1], [0, 5, -5])
    print(f"Shaded Intensity: {intensity}")

if __name__ == "__main__":
    main()
