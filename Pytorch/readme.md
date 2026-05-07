# NumPy vs PyTorch

| Feature | NumPy | PyTorch |
|---|---|---|
| Full Form | Numerical Python | Python Torch |
| Main Purpose | Numerical and scientific computing | Deep learning and tensor computation |
| Data Structure | ndarray | Tensor |
| GPU Support | ❌ No native GPU support | ✅ Yes (CUDA support) |
| Automatic Differentiation | ❌ Not available | ✅ Autograd support |
| Deep Learning Support | ❌ No | ✅ Yes |
| Neural Network Modules | ❌ No | ✅ `torch.nn` |
| Optimizers | ❌ No | ✅ `torch.optim` |
| Backpropagation | ❌ Manual | ✅ Automatic |
| Performance | Fast on CPU | Fast on CPU and GPU |
| Dynamic Computation Graph | ❌ No | ✅ Yes |
| Ease of Use for AI | Limited | Highly suitable |
| Used In | Data analysis, math operations | AI, ML, Deep Learning |
| Syntax Similarity | Base library | Very similar to NumPy |
| Developed By | Community | Meta (Facebook) |
| Typical Usage | Scientific computing | Neural network training |

---

What is Autograd in PyTorch?

Autograd is PyTorch’s automatic differentiation engine.

It automatically calculates:

### gradients (derivatives) of tensors
### used during backpropagation
### helps train neural networks

