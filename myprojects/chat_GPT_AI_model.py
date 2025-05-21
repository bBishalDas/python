#!/usr/bin/env python3
"""
AI Assistant
A simple voice-capable assistant to manage tasks, solve problems, and have casual conversation.

Features:
- Manage tasks and reminders (add, list, remove tasks).
- Answer simple math problems.
- Have casual conversations and tell jokes.
- Speak responses out loud (using pyttsx3).
- Optional: accept voice commands (using SpeechRecognition, if microphone is available).

Usage:
- Run `python ai_assistant.py` in a terminal.
- The assistant will prompt whether to enable voice commands.
- Interact via text input (and optionally voice) in the terminal.
- The assistant will speak its replies aloud.
- Tasks are saved to `tasks.json` for persistence.

Requirements:
- Python 3
- Libraries: pyttsx3, SpeechRecognition, pyaudio (for microphone), datetime, json
  (install with `pip install pyttsx3 SpeechRecognition pyaudio`)

Possible Extensions:
- More advanced natural language processing or machine learning.
- GUI interface or web app.
- Integration with calendars or external APIs (weather, news).
- i will become capable enough to make atleast this small AI.
"""

import pyttsx3
import speech_recognition as sr
import datetime
import time
import json
import os
import re
import random

class AIAssistant:
    def __init__(self):
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speed of speech (words per minute)
        
        # Initialize speech recognizer for voice input (if available)
        try:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
        except:
            self.recognizer = None
            self.microphone = None
        
        # File to store tasks
        self.tasks_file = 'tasks.json'
        # Load tasks if file exists, else start with empty list
        self.tasks = []
        if os.path.exists(self.tasks_file):
            try:
                with open(self.tasks_file, 'r') as f:
                    self.tasks = json.load(f)
            except Exception as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []
    
    def speak(self, text):
        """Speak the given text aloud and also print it to console."""
        print("Assistant:", text)
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen for a voice command and return it as text. Returns empty string if unavailable."""
        if not self.recognizer or not self.microphone:
            return ""
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            command = self.recognizer.recognize_google(audio)
            print("You (voice):", command)
            return command.lower()
        except Exception:
            print("Sorry, I didn't catch that.")
            return ""
    
    def save_tasks(self):
        """Save the current list of tasks to a JSON file."""
        try:
            with open(self.tasks_file, 'w') as f:
                json.dump(self.tasks, f)
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, task_desc, time_str=None):
        """Add a new task with an optional time string."""
        task = {'task': task_desc, 'time': time_str}
        self.tasks.append(task)
        self.save_tasks()
        if time_str:
            self.speak(f"Task '{task_desc}' added, scheduled at {time_str}.")
        else:
            self.speak(f"Task '{task_desc}' added to your tasks.")
    
    def list_tasks(self):
        """List all current tasks."""
        if not self.tasks:
            self.speak("You have no tasks at the moment.")
        else:
            self.speak("Here are your tasks:")
            for i, t in enumerate(self.tasks, 1):
                desc = t['task']
                time_str = t.get('time')
                if time_str:
                    print(f"{i}. {desc} at {time_str}")
                else:
                    print(f"{i}. {desc}")
    
    def remove_task(self, task_desc=None):
        """Remove a task by description (if given) or by asking for its number."""
        if not self.tasks:
            self.speak("You have no tasks to remove.")
            return
        if task_desc:
            # Attempt to find a task containing the given description
            matches = [t for t in self.tasks if task_desc.lower() in t['task'].lower()]
            if not matches:
                self.speak("No matching task found.")
                return
            if len(matches) > 1:
                self.speak("Multiple tasks match that description. Please be more specific.")
                return
            idx = self.tasks.index(matches[0])
        else:
            # Ask user for task number to remove
            self.speak("Which task number would you like to remove?")
            if self.recognizer and self.microphone:
                num_str = self.listen()
            else:
                num_str = input("Task number: ")
            if not num_str.isdigit():
                self.speak("I did not understand the number.")
                return
            idx = int(num_str) - 1
        
        # Remove the task if index is valid
        if 0 <= idx < len(self.tasks):
            removed = self.tasks.pop(idx)
            self.save_tasks()
            self.speak(f"Removed task: {removed['task']}")
        else:
            self.speak("That task number is out of range.")
    
    def check_reminders(self):
        """Check if any task's time is now, and trigger a reminder."""
        now = datetime.datetime.now().strftime("%H:%M")
        due_tasks = [t for t in self.tasks if t.get('time') == now]
        for t in due_tasks:
            self.speak(f"Reminder: {t['task']} (scheduled for now).")
            try:
                self.tasks.remove(t)
                self.save_tasks()
            except:
                pass
    
    def parse_math(self, text):
        """Detect and evaluate a math expression in the text (simple arithmetic)."""
        # If there's any operator or keyword 'calculate', attempt to evaluate
        if any(op in text for op in ['+', '-', '*', '/']) or 'calculate' in text:
            # Extract numeric expression characters
            expr = ''.join(re.findall(r"[0-9\+\-\*\/\.\(\) ]", text))
            try:
                result = eval(expr)
                self.speak(f"The result is {result}.")
            except Exception:
                self.speak("Sorry, I couldn't compute that expression.")
            return True
        return False
    
    def handle_command(self, command):
        """Process and respond to the user's command."""
        cmd = command.lower()
        # Greetings
        if any(greet in cmd for greet in ['hello', 'hi', 'hey']):
            self.speak("Hello! How can I assist you today?")
        elif 'how are you' in cmd:
            self.speak("I'm doing well, thank you!")
        elif 'your name' in cmd:
            self.speak("I am your AI assisstent.")
        # Time and date queries
        elif 'time' in cmd and 'date' not in cmd:
            now = datetime.datetime.now().strftime("%H:%M")
            self.speak(f"The current time is {now}.")
        elif 'date' in cmd:
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            self.speak(f"Today's date is {today}.")
        # Task management commands
        elif any(trigger in cmd for trigger in ['add task', 'remember to', 'set reminder']):
            # Parse patterns like "task at time"
            parts = cmd
            for phrase in ['add task', 'remember to', 'set reminder']:
                parts = parts.replace(phrase, '')
            parts = parts.strip()
            if ' at ' in parts:
                task_text, time_part = parts.rsplit(' at ', 1)
                self.add_task(task_text.strip(), time_part.strip())
            else:
                self.add_task(parts)
        elif 'list tasks' in cmd or 'show tasks' in cmd:
            self.list_tasks()
        elif any(x in cmd for x in ['remove task', 'delete task', 'done']):
            # Remove by description if provided, else ask
            term = cmd
            for phrase in ['remove task', 'delete task', 'done']:
                term = term.replace(phrase, '')
            term = term.strip()
            if term:
                self.remove_task(term)
            else:
                self.remove_task(None)
        # Math calculation
        elif self.parse_math(cmd):
            pass
        # Jokes
        elif 'joke' in cmd:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "I told my computer I needed a break, and it said: 'No problem, I'll go to sleep.'",
                "Why did the math book look sad? Because it had too many problems.",
                "your life.",
                "bhosiiri k chuup ray"
            ]
            self.speak(random.choice(jokes))
        # Polite responses
        elif 'thank' in cmd:
            self.speak("You're welcome!")
        elif 'bye' in cmd or 'goodbye' in cmd:
            self.speak("Goodbye! Have a great day!")
            return False
        elif 'help' in cmd:
            self.speak("I can help manage tasks, solve math problems, or just chat. Try 'add task ...', 'list tasks', 'calculate 2+2', or say 'joke'.")
        # If nothing matched, handle unknown
        else:
            if not self.parse_math(cmd):
                self.speak("I'm not sure how to respond to that. Can I help with something else?")
        return True
    
    def run(self):
        """Main loop to run the assistant."""
        self.speak("Hi, I'm your AI assisstent.")
        self.speak("I can help manage tasks, solve problems, or chat with you.")
        # Ask user if they want to enable voice input
        self.speak("Would you like to enable voice commands? (yes or no)")
        choice = input("Enable voice commands? (y/n): ").strip().lower()
        voice_enabled = (choice == 'y')
        
        while True:
            # Check for reminders that are due right now
            self.check_reminders()
            
            # Get user command (voice or text)
            if voice_enabled:
                user_input = self.listen()
                if not user_input:
                    user_input = input("You: ")
                else:
                    print(f"You: {user_input}")
            else:
                user_input = input("You: ")
            
            if not user_input:
                continue
            
            # Process the command
            continue_chat = self.handle_command(user_input)
            if not continue_chat:
                break

if __name__ == "__main__":
    assistant = AIAssistant()
    assistant.run()
