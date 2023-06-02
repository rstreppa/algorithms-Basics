/**
In computer science, a priority queue is an abstract data type which is like a regular queue, but where additionally each element has a "priority" associated with it. 
In a priority queue, an element with high priority is served before an element with low priority. - Wikipedia

In this problem we will test your knowledge on Java Priority Queue.

There are a number of students in a school who wait to be served. Two types of events, ENTER and SERVED, can take place which are described below.

ENTER: A student with some priority enters the queue to be served.
SERVED: The student with the highest priority is served (removed) from the queue.
A unique id is assigned to each student entering the queue. The queue serves the students based on the following criteria (priority criteria):

The student having the highest Cumulative Grade Point Average (CGPA) is served first.
Any students having the same CGPA will be served by name in ascending case-sensitive alphabetical order.
Any students having the same CGPA and name will be served in ascending order of the id.
Create the following two classes:

The Student class should implement:
The constructor Student(int id, String name, double cgpa).
The method int getID() to return the id of the student.
The method String getName() to return the name of the student.
The method double getCGPA() to return the CGPA of the student.
The Priorities class should implement the method List<Student> getStudents(List<String> events) to process all the given events and return all the students yet to be served in the priority order.
Input Format

The first line contains an integer, , describing the total number of events. Each of the  subsequent lines will be of the following two forms:

ENTER name CGPA id: The student to be inserted into the priority queue.
SERVED: The highest priority student in the queue was served.
The locked stub code in the editor reads the input and tests the correctness of the Student and Priorities classes implementation.

Constraints

Output Format

The locked stub code prints the names of the students yet to be served in the priority order. If there are no such student, then the code prints EMPTY.

*/

import java.util.ArrayList; 
import java.util.List; 
import java.util.Scanner; 
import java.util.PriorityQueue;

class Student implements Comparable<Student> { 
    private int id; 
    private String name; 
    private double cgpa;
    
    public Student(int id, String name, double cgpa) {
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }

    @Override
    public int compareTo(Student other) {
        if (this.cgpa != other.cgpa) {
            return Double.compare(other.cgpa, this.cgpa);
        } else if (!(this.name.equals(other.name))) {
            return this.name.compareTo(other.name);
        } else {
            return this.id - other.id;
        }
    }
    
    public String getName() {
        return this.name;
    }

    
}

class Priorities { 
    public List<Student> getStudents(List <String> events) { 
        PriorityQueue<Student> queue = new PriorityQueue<>();
        for (String each: events) {
            String[] arr = each.split(" ");
            String type = arr[0];

            if (type.equalsIgnoreCase("ENTER")) {
                String name = arr[1];
                double cgpa = Double.parseDouble(arr[2]);
                int id = Integer.parseInt(arr[3]);

                queue.add(new Student(id, name, cgpa));

            } else if (type.equalsIgnoreCase("SERVED")) {
                queue.poll();
            }
        }
        List<Student> students = new ArrayList<>();

        while (!queue.isEmpty()) {
            students.add(queue.poll());
        }

        return students;
    }        

}

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in); 
        Priorities priorities = new Priorities();
        int totalEvents = Integer.parseInt(scan.nextLine());
        List<String> events = new ArrayList<>();

        while (totalEvents-- != 0) {
            String event = scan.nextLine();
            events.add(event);
        }

        List<Student> students = priorities.getStudents(events);

        if (students.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Student st: students) {
                System.out.println(st.getName());
            }
        }         
    }
}
