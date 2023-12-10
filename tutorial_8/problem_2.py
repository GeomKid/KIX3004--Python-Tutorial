class Vector3D:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: "Vector3D"):
        return Vector3D(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def __mul__(self, other: "Vector3D"):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return f"[X={self.x},Y={self.y},Z={self.z}]"
