/*************************************************************************
	> File Name: myQueue.java
	> Author: kangshaoshun
	> Mail: kangshaoshun@gmail.com 
	> Created Time: 2017年11月01日 星期三 14时44分35秒
 ************************************************************************/
import java.util.Stack;
public class myQueue{
	//提供以下几个方法：
	//	1.add  入队
	//	2.pull 出队
	//	3.peek 队首元素
	private Stack<Integer> stackIn = new Stack<Integer>();
	private Stack<Integer> stackOut = new Stack<Integer>();

	public void add(int value){
		this.stackIn.push(value);
	}

	public int pull(){
		if(this.stackOut.isEmpty()){
			if(stackIn.isEmpty())throw new RuntimeException("Queue is Empty");
			while(! this.stackIn.isEmpty()){
				this.stackOut.push(this.stackIn.pop());
			}
		}
			return this.stackOut.pop();
		}

	public int peek(){
		if(this.stackOut.isEmpty()){
			if(this.stackIn.isEmpty()){
				throw new RuntimeException("Queue is Empty");
			}
			while(! this.stackIn.isEmpty()){
				this.stackOut.push(this.stackIn.pop());
			}
		}
		return this.stackOut.peek();
	}


}
