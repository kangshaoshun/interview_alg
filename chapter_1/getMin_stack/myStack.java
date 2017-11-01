/*************************************************************************
	> File Name: myStack.java
	> Author: kangshaoshun
	> Mail: kangshaoshun@gmail.com 
	> Created Time: 2017年11月01日 星期三 09时43分53秒
 ************************************************************************/
import java.util.Stack;
public class myStack{
	private Stack<Integer> stackData;
	private Stack<Integer> stackMin;
	
	public myStack(){
		this.stackData = new Stack<Integer>();
		this.stackMin = new Stack<Integer>();
	}

	public int pop(){
		if(this.stackData.isEmpty())return -1;
		int value = this.stackData.pop();
		if(value == this.stackMin.peek())this.stackMin.pop();
		return value;
	}

	public void push(int value){
		this.stackData.push(value);
		if(this.stackMin.isEmpty() || this.stackMin.peek() > value){
			this.stackMin.push(value);
		}
	}
	public int getMin(){
		return this.stackMin.peek();
	}

}
