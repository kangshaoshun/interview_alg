/*************************************************************************
	> File Name: stackSort.java
	> Author: kangshaoshun
	> Mail: kangshaoshun@gmail.com 
	> Created Time: 2017年11月04日 星期六 10时56分27秒
 ************************************************************************/
import java.util.Stack;
public class stackSort{
	public static void main(String[] args){
		Stack<Integer> s = new Stack<Integer>();
		Stack<Integer> h = new Stack<Integer>();
		s.push(2);
		s.push(4);
		s.push(3);
		s.push(1);
		s.push(5);
		while(!s.isEmpty()){
			int cur = s.pop();
			if(h.isEmpty() || h.peek() >= cur)h.push(cur);
			else{
				while(!h.isEmpty() && h.peek() < cur)s.push(h.pop());
				h.push(cur);
			}
		}
		while(!h.isEmpty())s.push(h.pop());
		while(!s.isEmpty())System.out.println(s.pop());
	}
}
