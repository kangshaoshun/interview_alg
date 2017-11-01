/*************************************************************************
	> File Name: test.java
	> Author: kangshaoshun
	> Mail: kangshaoshun@gmail.com 
	> Created Time: 2017年11月01日 星期三 15时18分34秒
 ************************************************************************/
import java.util.Stack;
public class test{
	public static int reverse_stack(Stack<Integer> stack){
		int result = stack.pop();
		if(stack.isEmpty())return result;
		else{
			int last = reverse_stack(stack);
			stack.push(result);
			return last;
		}
	}

	public static void reverse(Stack<Integer> stack){
		if(stack.isEmpty())return;
		int result = reverse_stack(stack);
		reverse(stack);
		stack.push(result);
	}

	public static void main(String[] args){
		Stack<Integer> stack = new Stack<Integer>();
		stack.push(1);
		stack.push(2);
		stack.push(3);
		reverse(stack);
		System.out.println(stack.peek());
	}
}
