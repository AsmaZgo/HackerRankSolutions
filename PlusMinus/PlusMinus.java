import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Result {

    /*
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

     public static void plusMinus(List<Integer> arr) {

        float  minuscount=0;
        float pluscount=0;
        float zerocount=0;
        DecimalFormatSymbols formatSymbols = new
                DecimalFormatSymbols(Locale.getDefault());
        formatSymbols.setDecimalSeparator('.');
        formatSymbols.setGroupingSeparator(' ');
        String pattern = "####.######";
        DecimalFormat decimalFormat = new DecimalFormat(pattern, formatSymbols);

        for (int i=0;i<arr.size();i++) {

            //verif conditions
            if(arr.get(i)>100 || arr.get(i)<-100){

                try {
                    throw new Exception("wrong format");
                } catch (Exception e) {
                    e.printStackTrace();
                } 
            }
            if(arr.get(i)>0)
                pluscount++;
            else if(arr.get(i)<0)
                minuscount++;
            else
                zerocount++;
        }
        String number = decimalFormat.format(pluscount/arr.size());
 
        System.out.println(number);

 
        number = decimalFormat.format(minuscount/arr.size());
        System.out.println(number);
 
        number = decimalFormat.format(zerocount/arr.size());
        System.out.println(number);

    }

}
public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        String[] arrTemp = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        List<Integer> arr = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrTemp[i]);
            arr.add(arrItem);
        }

        Result.plusMinus(arr);

        bufferedReader.close();
    }
}
