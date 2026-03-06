#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
      if(nums.empty()) return 0;
      
      for(int i=0;i<nums.size();i++){
        if(nums[i]==target){
            return i;
        }
        else if(nums[i]>target){
             return i;
        }
               
      }
    
      
       return nums.size();
    }
};
/*better solution-
int left = 0, right = nums.size() - 1;
while (left <= right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] == target) return mid;
    else if (nums[mid] < target) left = mid + 1;
    else right = mid - 1;
}
return left; */ 