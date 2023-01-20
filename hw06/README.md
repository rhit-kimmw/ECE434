# HW06
### Martino Kim


---

>'modules' and 'rt' folders are the example folders from the examples repository.

>'rt' folder contains the files for history files(nort_load, nort_noload, rt_load, rt_noload) and the resulted plots(NoN_RT, RT).

>'./longTask.py' is a python file which unlimitedly prints a number, which is used for a long task.

---

1. Julia Cartwright works at National Instruments

2. PREEMT_RT is a linux kernel designed to maintain low latency, consistent response time, and determinism.

3. Mixed criticality is a system with hardware and software to executed different type of tasks with different time criticality or safety criticality to run and communicate together.

4. Drivers can have a long running interrupts in mainline to prevent other critical threads from running immediately.

5. $\delta$ is a real time latency for an event to occur to execute an application.

6. Cyclictest is a tool for evaluating the relative performance of real-time systems.

7. Figure 2 shows the plot of preempt vs preempt_rt, and shows that preempt_rt has better performance.

8. Displatch latency is time latency between the task fired from the hardware to be told to run by the scheduler.Scheduling latency is time latency between the task asked to run by the scheduler to the CPU to execute the task.

9. mainline is a main schedule for tasks.

10. External event is prevented because low priority interrupt is executing in the CPU.

11. External event is started because the code allows the handler threads to be scheduled immediately after the event.

--- 

## PREEMPT_RT

> The plots are generated. One for No RT, and one for with RT.

> The RT kernel definitely shuts down the continued ripples that you can see in the NON-RT.

![NON-RT](NoN_RT.png)

![with_RT](RT.png)