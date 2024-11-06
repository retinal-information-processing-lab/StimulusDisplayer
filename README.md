<h1 style="margin-bottom: 0px; font-size: 36px">Stimulus Displayer</h1>
<h3 style="margin-top: 0px;font-size: 25px">and Setup Guide</h3>

This notebook allows you to read and verify whether your stimulus is being displayed properly. It checks if the sequence settings are correct, and enables the creation of GIFs to visualize the stimulus output.

### File and Folder Setup 

Before running the notebook, ensure the following files and folders are properly set up in your working directory:

- **VEC Folder**: Contains `.vec` files (which describe the sequences of frames).
- **BIN Folder**: Contains `.bin` files (which store the visual frames to be displayed).
- **StimList Folder**: For VDH stimulus setups, include the **phasmasks list** here.
- **MEA Setup**: A setup description is needed to correctly read the `.bin` file (typically provided by the stimulus generation system).
- **Frame Rate**: The frame rate is set based on the GUI maximum (typically about 100Hz, but this can vary depending on your computer's performance).

### Sequence Selection

The notebook allows you to select which stimulus sequences you want to display in the GUI.

- The **VEC file** contains information about each sequence, with each line representing a frame triggered on the DMD (Digital Micromirror Device). The first line of the `.vec` file is a summary, and the next lines follow this structure (left to right column):
  - `(0 : nothing, 1 : switch the next phasemask)` 
  - `(visual frame index in the bin file)`
  - `(reserved for future color settings)`
  - `(0 : laser shutter close, 1 : laser shutter open)`
  - `(sequence number with repetition number added to it)`

### Steps for Using the Notebook
1. **Enter parameters**: You will first have to enter to right bin, vec, phasemask file, mea and frame rate
2. **Select Sequences**: You can choose specific sequences to display in the GUI (one or more sequences number separatd with space or ,), or display all available sequences (empty input).
3. **Display the GUI**: After selecting your sequences, the GUI will display the stimuli. During the display, the last 10 seconds of the stimulus will be captured and saved as frames. If while playing the visual stimulus, the vec calls for a non existing frame in the bin, an error message is displayed and the unknown frame is replace by the first frame of the bin.
4. **Create a GIF**: The captured frames can be used to create a GIF of the visual stimulus to ensure that the sequence is displayed correctly.
5. **Generate GIF for All Sequences**: After confirming the visual display, you can generate a GIF for the every visual stimulus based on the `.vec` file sequences, one gif per sequence.


### Installation process

You will need a simple python environement with jupyter notebook and pygame installed
