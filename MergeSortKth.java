class Solution {
    public boolean debug = false;
    public int findKthLargest(int[] nums, int k) {
        int low = 0;
        int high = nums.length - 1;
        mergesort(nums, low, high);
        return nums[high - k + 1];
    }
    
    public void mergesort(int[] nums, int low, int high) {
        if (low < high) {
            int mid = (low + high) / 2;
            mergesort(nums, low, mid);
            mergesort(nums, mid + 1, high);
            merge(nums, low, high, mid);
        }
    }
    
    public void merge(int[] nums, int low, int high, int mid) {
        int[] temp = new int[high - low + 1];
        int left = low;
        int right = mid + 1;
        int i = 0;
        while ((left <= mid) && (right <= high)) {
            if (debug) {
                System.out.println("nums.length = " + nums.length);
                System.out.println("left = " + left);
                System.out.println("right = " + right);
            }
            if (nums[left] < nums[right]) {
                temp[i++] = nums[left++];
            } else {
                temp[i++] = nums[right++];
            }
        }
        while (left <= mid) {
            temp[i++] = nums[left++];
        }
        
        while (right <= high) {
            temp[i++] = nums[right++];
        }
        
        for (int n = low; n <= high; n++) {
            nums[n] = temp[n - low];
        }
    }
}

public class MergeSortKth {
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