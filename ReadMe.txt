# Typing Speed Test

A desktop application built with Python and Tkinter that measures typing speed and accuracy through a timed typing challenge. Using a randomly selected set of common English words, the application tracks typing performance and displays results when the test ends.

## Features

- Timed Challenge: Complete a 60-second typing test.
- Randomised Word List: Practise using 100 randomly selected words from a dataset of 1,200 commonly used English words.
- Real-Time Feedback: Highlight the current word to help users follow their progress.
- Performance Metrics: Calculate characters per minute (CPM), correctly typed characters per minute, and words per minute (WPM).
- Results Popup: Display performance statistics when the timer expires.
- Restart Functionality: Reset the test and try again.

## Technologies

- Python
- Tkinter
- Pandas
- CSV data handling

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SinceSlicedBread/typing-speed-test.git
   ```

2. Navigate to the project directory:

   ```bash
   cd typing-speed-test
   ```

3. Install the required dependency:

   ```bash
   pip install pandas
   ```

4. Run the application:

   ```bash
   python main.py
   ```

## How to Play

1. Launch the application.
2. Type the displayed words into the input field.
3. Continue typing as accurately and quickly as possible until the timer reaches zero.
4. Review your results in the summary popup.
5. Select Restart to attempt another test.

## Scoring

- Characters Per Minute (CPM): Total characters typed per minute.
- Correct Characters Per Minute: Correctly typed characters per minute.
- Words Per Minute (WPM): Correctly typed characters divided by five.

## Purpose

This project demonstrates Python GUI development, event-driven programming, timer management, text processing, data handling with Pandas, and performance metric calculations.