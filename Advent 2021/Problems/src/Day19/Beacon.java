package Day19;

public class Beacon {
    public int x;
    public int y;
    public int z;

    public Beacon(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public Beacon(Beacon one, Beacon two) {
        this(one.x - two.x, one.y - two.y, one.z - two.z);
    }

    public Beacon up(int up) {
        return switch (up) {
            case 0 -> new Beacon(x, y, z);
            case 1 -> new Beacon(y, z, x);
            case 2 -> new Beacon(z, x, y);
            case 3 -> new Beacon(-x, z, y);
            case 4 -> new Beacon(z, y, -x);
            case 5 -> new Beacon(y, -x, z);
            case 6 -> new Beacon(x, z, -y);
            case 7 -> new Beacon(z, -y, x);
            case 8 -> new Beacon(-y, x, z);
            case 9 -> new Beacon(x, -z, y);
            case 10 -> new Beacon(-z, y, x);
            case 11 -> new Beacon(y, x, -z);
            case 12 -> new Beacon(-x, -y, z);
            case 13 -> new Beacon(-y, z, -x);
            case 14 -> new Beacon(z, -x, -y);
            case 15 -> new Beacon(-x, y, -z);
            case 16 -> new Beacon(y, -z, -x);
            case 17 -> new Beacon(-z, -x, y);
            case 18 -> new Beacon(x, -y, -z);
            case 19 -> new Beacon(-y, -z, x);
            case 20 -> new Beacon(-z, x, -y);
            case 21 -> new Beacon(-x, -z, -y);
            case 22 -> new Beacon(-z, -y, -x);
            case 23 -> new Beacon(-y, -x, -z);
            case 24 -> new Beacon(x, -y, z);
            case 25 -> new Beacon(-x, y, z);
            case 26 -> new Beacon(x, y, -z);
            //case 27 -> new Beacon(-y, -x, -z);
            //case 28 -> new Beacon(-y, -x, -z);
            //case 29 -> new Beacon(-y, -x, -z);
            default -> null;
        };
    }

    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Beacon Beacon = (Beacon) o;
        return x == Beacon.x && y == Beacon.y && z == Beacon.z;
    }

    public String toString() {
        return (x + " " + y + " " + z);
    }
}
