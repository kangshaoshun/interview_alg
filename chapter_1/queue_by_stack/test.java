/*************************************************************************
	> File Name: test.java
	> Author: kangshaoshun
	> Mail: kangshaoshun@gmail.com 
	> Created Time: 2017年11月01日 星期三 14时53分36秒
 ************************************************************************/
public class test{
	public static void main(String[] args){
		myQueue queue = new myQueue();
		queue.add(1);
		queue.add(2);
		queue.add(3);
		System.out.println(queue.pull());
		System.out.println(queue.peek());
		System.out.println(queue.pull());
		System.out.println(queue.peek());
		System.out.println(queue.pull());
		System.out.println(queue.pull());
	}
}
