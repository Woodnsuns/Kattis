class Solution {
    public boolean debug = true;
    public int findKthLargest(int[] nums, int k) {
        quickSort(nums, 0, nums.length - 1);
        if (debug) {
            for (int i = 0; i < nums.length; i++) {
                System.out.println(nums[i]);
            }
        }
        return nums[nums.length - k];
    }
    
    public void quickSort(int[] nums, int i, int j) {
        if (i < j) {
            int piv = partition(nums, i, j);
            quickSort(nums, i, piv - 1);
            quickSort(nums, piv + 1, j);
        }
    }
    
    public int partition(int[] a, int i, int j) {
        int pivot = a[i];
        int bound = i + 1;
        for (int n = i + 1; n <= j; n++) {
            if (a[n] < pivot) {
                swap(a, n, bound);
                bound++;
            }
        }
        swap(a, i, bound - 1);
        return (bound - 1);
    }
    
    public void swap(int[] a, int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}

public class QuickSortKth {
    public static int[] stringToIntegerArray(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) {
          return new int[0];
        }
    
        String[] parts = input.split(",");
        int[] output = new int[parts.length];
        for(int index = 0; index < parts.length; index++) {
            String part = parts[index].trim();
            output[index] = Integer.parseInt(part);
        }
        return output;
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int[] nums = stringToIntegerArray(line);
            line = in.readLine();
            int k = Integer.parseInt(line);
            
            int ret = new Solution().findKthLargest(nums, k);
            
            String out = String.valueOf(ret);
            
            System.out.print(out);
        }
    }
}