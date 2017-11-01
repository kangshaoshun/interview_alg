/*************************************************************************
	> File Name: test.java
	> Author: kangshaoshun
	> Mail: kangshaoshun@gmail.com 
	> Created Time: 2017年11月01日 星期三 09时44分17秒
 ************************************************************************/
import java.util.Stack;
public class test{
	public static void main(String[] args){
		myStack s = new myStack();
		s.push(1);
		s.push(3);
		System.out.println(s.getMin());
		s.push(2);
		System.out.println(s.pop());
		s.push(0);
		System.out.println(s.getMin());

	}
}
