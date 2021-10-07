# https://leetcode.com/problems/combination-sum/

class Solution {
    vector<vector<int>> ans;
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> current;
        dfs( 0, candidates, current, target);
        return ans;
    }
    
    void dfs( int index, vector<int>& candidates, vector<int>& current, int target){
        if(target < 0)
            return;
        if(target == 0)
        {
            ans.push_back(current);
            return;
        }
        
        for(int i=index; i<candidates.size();i++){
            current.push_back(candidates[i]);
            dfs(i, candidates, current, target-candidates[i]);
            current.pop_back();
        }
    }
};
