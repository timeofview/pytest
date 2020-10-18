import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Server {

    public static void main(String[] args) {
        System.out.print("Args ");
        Arrays.stream(args).forEach(System.out::println);
        while(true){
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("1 sec");
        }
    }
}
