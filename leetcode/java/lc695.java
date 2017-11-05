/*************************************************************************
	> File Name: 695.java
	> Author: kangshaoshun
	 Mail: kangshaoshun@gmail.com 
	> Created Time: 2017年11月04日 星期六 21时00分41秒
 ***********************************************************************
 */
public class lc695{
	/*
	 * Time Complexity:O(mn)
	 * Space Complexity:O(mn)
	*/
	public int find(int[][] grid, int x, int y, int[][] visited){
		if(grid[x][y] == 0 || visited[x][y] == 1)return 0;
		if(x+1 < grid.length)result += find(grid, x+1, y, visited);
		if(x-1 >= 0) result += find(grid, x-1, y, visited);
		if(y+1 < grid[0].length)result += find(grid, x, y+1, visited);
		if(y-1 >= 0)result += find(grid, x, y-1, visited);
		return result;
	}


	public int getMaxArea(int[][] grid){
		if(grid == null || grid.length == 0)return 0;
		int[][] visited = new int[grid.length][grid[0].length];
		int max = 0;
		for (int i = 0; i < grid.length; i++){
			for(int j = 0; j < grid[0].length; j++){
				if(grid[i][j] == 0)continue;
				result = find(grid, i , j, visited);
				if(result > max)max = result;
			}
		}
		return max;
	}

	public static void main(String[] args){
		
	}
}
