# Parallel Processing in ML

---

## Why do we need Parallel processing ?

In order to make the training process faster we are going to need some performance metrics to measure it. The term performance in these systems has a double interpretation. 

On the one hand, it refers to the predictive accuracy of the model. On the other, to the computational speed of the process.

The accuracy is independent of the platform, and it is the performance metric to compare multiple models. In contrast, the computation speed depends on the platform on which the model is deployed

### Important Metrics are :

- **Speedup** :  The ratio of solution time for the sequential (or 1 GPU) algorithms versus its parallel counterpart (with many GPUs). 

- **Throughput** : The number of images per unit time that can be processed. This can give us a good benchmark of performance

- **Scalability** :  It is a more generic concept that refers to the ability of a system to handle a growing amount of work efficiently.


The main idea behind this computing paradigm is to run tasks in parallel instead of serially, as it would happen in a single machine.

## Parallel computer platforms
- DNN are often compute-intensive, making them similar to traditional supercomputing (high-performance computing, HPC) applications.

*Hence Multiple GPUs increase both memory and compute available for training a DNN. In a nutshell, we have several choices, given a minibatch of training data that we want to classify.*


## Types of parallelism
---
To achieve the distribution of the training step, there are two principal implementations, and it will depend on the needs of the application to know which one will perform better, or even if a mix of both approaches can increase the performance.


1. ### ***Model parallelism*** :
Different layers in a Deep Learning model may be trained in parallel on different GPUs. This training procedure is commonly known as Model parallelism.<br/><br/>


![Model-Parallelism](https://miro.medium.com/max/1036/1*ysnR6M7v_Mt_5mEI4JAIAQ.jpeg)
<br/><br/>
- In this case (also known as Network Parallelism), the model will be segmented into different parts that can run concurrently, and each one will run on the same data in different nodes. 

- This method’s scalability depends on the degree of task parallelization of the algorithm, and it is more complex to implement than the previous one. 

- It may decrease the communication needs, as workers need only to synchronize the shared parameters (usually once for each forward or backward-propagation step) and works well for GPUs in a single server that shares a high-speed bus. It can be used with larger models as hardware constraints per node are no more a limitation.

2. ### ***Data parallelism*** :
 We use the same model for every execution unit, but train the model in each computing device using different training samples.<br/>

![Data-Parallelism](https://miro.medium.com/max/401/1*Fk9LVHl9eoATot15eVXUsA.jpeg) /
<br/>

***In general, the parallelization of the algorithm is more complex to implement than run the same model in a different node with a subset of data.***

## ***Deep into Data Parallelism***
---

###  *Synchronous versus asynchronous distributed training*

- Stochastic gradient descent (SGD) is an iterative algorithm that involves multiple rounds of training, where the results of each round are incorporated into the model in preparation for the next round. 
- The rounds can be run on multiple devices, either synchronously or asynchronously.
Each SGD iteration runs on a mini-batch of training samples. 
- In  <font size = 4>***Synchronous training*** </font> , all the devices train their local model using different parts of data from a single (large) mini-batch. They then communicate their locally calculated gradients (directly or indirectly) to all devices. 
- Only after all devices have successfully computed and sent their gradients th model is updated. The updated model is then sent to all nodes along with splits from the next mini-batch.

- In <font size = 4>***Asynchronous training*** </font>, no device waits for updates to the model from any other device. The devices can run independently and share results as peers or communicate through one or more central servers known as “parameter” servers. 
- In the peer architecture, each device runs a loop that reads data, computes the gradients, sends them (directly or indirectly) to all devices, and updates the model to the latest version.

## Parameter distribution and communication in synchronous training

*For synchronous training, we can choose between two main schemes: centralized or decentralized.*

*The choice between designing a centralized and a decentralized scheme for DNN training depends on multiple factors, including the network topology, bandwidth, communication latency, parameter update frequency, or desired fault tolerance.*

## ***Centralized***
The centralized scheme would typically include a so-called Parameter Server strategy.

![Centralised](https://miro.medium.com/max/3000/1*7WfWLkeL7XJnua2IRymZiA.png)

- When parallel SGD uses parameter servers, the algorithm starts by broadcasting the model to the workers (servers). 
- Each worker reads its own split from the mini-batch in each training iteration, computing its own gradients, and sending those gradients to one or more parameter servers. 
- The parameter servers aggregate all the gradients from the workers and wait until all workers have completed before they calculate the new model for the next iteration, which is then broadcasted to all workers.

## ***De-Centralized***

![DeCentralised](https://miro.medium.com/max/3000/1*tSBqypuo2F4vSUHSOuDbfg.png)

- The decentralized scheme would rely on ring-allreduce to communicate parameter updates among the nodes. 
- In the ring-allreduce architecture, there is no central server that aggregates gradients from workers. 
- Instead, in a training iteration, each worker reads its own split for a mini-batch, calculates its gradients, sends its gradients to its successor neighbor on the ring, and receives gradients from its predecessor neighbor on the ring.


# Scalable Deep Learning Frameworks
 ---

***There are software libraries, known as DL Frameworks, that facilitate this parallelization or distribution.***

## Parallel training in one server

***We can use frameworks as TensorFlow of Pytorch to program multi-GPU training in one server. To parallelize the training of the model, you only need to wrap the model with***

``` torch.nn.parallel.DistributedDataParallel ``` ***- in PyTorch***
and with 
```tf.distribute.MirroredStrategy``` ***in TensorFlow***


##  Distributed training in multiple server
***However, the number of GPUs that we can place in a server is very limited, and the solution goes through putting many of these servers together, as we did at the BSC, with the CTE-POWER supercomputer, where 54 servers are linked together with an InfiniBand network on optical fiber.***

***In this new scenario, we need an extension of the software stack to deal with multiple distributed GPUs in the neural network training process.***
