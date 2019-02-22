import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class IO {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static String[] buffers = new String[1];
    private static int cur=1;

    static BufferedReader getBr() {
        return br;
    }

    static String next() {
        String res = null;
        try {
            res = br.readLine();
            cur = buffers.length;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return res;
    }

    static int nextInt() {
        if(buffers.length == cur) {
            buffers = next().split(" ");
            cur = 0;
        }
        return Integer.parseInt(buffers[cur++]);
    }

    static long nextLong() {
        if(buffers.length == cur) {
            buffers = next().split(" ");
            cur = 0;
        }
        return Long.parseLong(buffers[cur++]);
    }

    static double nextDouble() {
        if(buffers.length == cur) {
            buffers = next().split(" ");
            cur = 0;
        }
        return Double.parseDouble(buffers[cur++]);
    }

    static void out(Object... obj) {
        StringBuilder sb = new StringBuilder();
        for(Object o:obj) {
            sb.append(o);
        }
        System.out.println(sb);
    }

    static void outs(Object... obj) {
        StringBuilder sb = new StringBuilder();
        sb.append(obj[0]);
        for(int i=1; i<obj.length; i++) {
            sb.append(" ").append(obj[i]);
        }
        System.out.println(sb);
    }
}

public class Main {

    public static void main(String[] args) {
        IO.out();
    }
}
