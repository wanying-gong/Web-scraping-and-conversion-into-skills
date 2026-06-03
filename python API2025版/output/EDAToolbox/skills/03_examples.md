# Examples
> **说明：** Examples 相关页面。

> **何时使用：** 当你需要查阅 Examples 相关内容时

---

## 本文件目录

- **Examples** (`Examples/index.md`)

---

<!-- === 来源: Examples/index.md === -->

# Examples[](#examples "Link to this heading")

This guide will go through how to run the examples that are included in the toolbox.
We will assume that you have installed the toolbox, instructions on how to successfully do so are found in the [Initial Setup](../Initial_Setup/installation.md).

Note

Certain examples require additional python packages to be installed. Instructions on which packages, and how they can be installed, are found in the [Verifying Installation](../Initial_Setup/verifying.md) section.

Note

Certain examples require additional products to be installed, such as SystemVue or VSA.

## Get the example workspaces[](#get-the-example-workspaces "Link to this heading")

Download the example workspaces from the [Knowledge Center](https://docs.keysight.com/pages/viewpage.action?pageId=762705202).

Assume you have put these files in your “f:/temp/edatoolbox” directory.
Use a command prompt to navigate to this directory.

## Running the examples[](#running-the-examples "Link to this heading")

Next we need to choose which example to run, and where to write the output to.
Assume the output directory is “f:/temp/edatoolbox/output”.
Run the choses example using python.

```
>>> py <example>.py --output-dir=f:/temp/edatoolbox/output
```

Note

Certain examples require xxPro’s python to be used. If this is the case, make sure the toolbox and any other required packages are installed in xxPro’s distribution. And call python using `python` instead of `py`.


---

