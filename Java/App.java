package Java;

import java.io.BufferedReader;
import java.io.InputStreamReader;

class App {
      public static void main(String a[]) {
            try {
                  // Montador e inicializador do input
                  ProcessBuilder montador = new ProcessBuilder(
                              // linguagem
                              "python",
                              // 0 diretório
                              System.getProperty("user.dir") + "\\Python\\Calculadora.py",
                              // 1... variáveis
                              "28", "15");
                  Process comando = montador.start();

                  // Inicializa o leitor
                  BufferedReader leitorA = new BufferedReader(new InputStreamReader(comando.getInputStream()));
                  BufferedReader leitorB = new BufferedReader(new InputStreamReader(comando.getErrorStream()));

                  // loop (enquanto tem informação mostra a linha)
                  String linha = null;
                  while ((linha = leitorA.readLine()) != null) {
                        System.out.println("linha - " + linha);
                  }
                  // loop (se der null no meio do código)
                  while ((linha = leitorB.readLine()) != null) {
                        System.out.println("erro linha - " + linha);
                  }

                  // caso dér erro fatal
            } catch (Exception e) {
                  System.out.println(e);
            }
      }
}
