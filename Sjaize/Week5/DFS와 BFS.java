import java.io.*;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    static StringBuilder sb = new StringBuilder();
    static int[][] graph;
    static boolean[] visited;
    static Queue<Integer> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());

        graph = new int[n+1][n+1];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        visited = new boolean[n+1];
        dfs(v);

        sb.append("\n");

        visited = new boolean[n+1];
        bfs(v);

        System.out.println(sb);
    }

    private static void dfs(int start) {
        visited[start] = true;
        sb.append(start + " ");
        for (int i = 0; i < graph.length; i++) {
            if (graph[start][i] == 1 && !visited[i]) {
                dfs(i);
            }
        }
    }

    private static void bfs(int start) {
        queue.add(start);
        visited[start] = true;
        sb.append(start + " ");

        while(!queue.isEmpty()) {
            int nodeIndex = queue.poll();

            for (int next = 0; next < graph[nodeIndex].length; next++) {
                if (graph[nodeIndex][next] == 1 && !visited[next]) {
                    queue.add(next);
                    visited[next] = true;
                    sb.append(next + " ");
                }
            }
        }
    }
}
