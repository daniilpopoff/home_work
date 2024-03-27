public class RootDichotomyMethod {
    // Function: f(x) = e^(-x) - x
    public static double function(double x) {
        return Math.exp(-x) - x;
    }

    // Dichotomy method to solve the equation f(x) = 0
    public static double dichotomyMethod(double a, double b, double epsilon) {
        double left = a;
        double right = b;
        double mid;

        while ((right - left) > epsilon) {
            mid = (left + right) / 2;


            if (function(b)*function(mid)<0){
                left = mid;
            }
            else  {
                right = mid;
            }

//            else {
//                return mid;
//            }
        }
        return (left + right) / 2;
    }

    public static void main(String[] args) {
        double a = -1; // Left end of the interval
        double b = 1; // Right end of the interval
        double epsilon = 0.1; // Accuracy

        double root = dichotomyMethod(a, b, epsilon);
        System.out.println("Root of the equation e^(-x) - x = 0 is approximately: " + root);
    }
}
