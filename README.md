# washington-quarter-id

A tool for identifying coins using machine vision techniques

## Pipeline

Completing this task will require a series of steps that process the input image.
I'd like to experiment with functional programming principles
to maintain a manageable codebase.
Each step of the pipeline could be implemented as a "pure" function,
that means that they won't modify their inputs or any global state.

I think we'll need the following functions:

- [ ] A function that takes the original image as an input,
  and returns the list of all circle locations and sizes in that image (coin locations).
- [ ] A function that takes the original image and a list of circles as input,
  and returns a collection of smaller square images, each one containing a coin.
- [ ] A function that takes a single image of a coin as input,
  and returns that same image with any background noise removed.
- [ ] And many more! (TODO)