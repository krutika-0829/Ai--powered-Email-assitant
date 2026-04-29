# Ai--powered-Email-assitant

# Project Overview
An AI-powered Email Assistant built using **FastAPI**, **Streamlit**, and an open-source LLM (**Mistral via Ollama**). It can Summarize Emails , detect Tone and genrate intelligent replies based on tone and context.

# Features

## Email Summarization
Generates a short and simple summary of long emails.

## Tone Detection
Detects the tone of an email.

Supported tones:
- Formal
- Informal
- Angry
- Polite
- Neutral

## Smart Reply Generation
Generates context-aware replies while matching the tone of the original email.

Examples:
- Informal email → casual reply
- Formal email → professional reply
- Angry email → calm and polite response

# Tech Stack

- Python
- FastAPI
- Streamlit
- Ollama
- Mistral LLM
- Pydantic

# Request Email
Subject: Catching up

Hey,

It’s been a while! Just wanted to check in and see how things are going on your end. Let’s catch up sometime this week if you’re free.

Cheers!

# Response
- Summarize : Output: {'Summary': "The sender is checking in after some time, wanting to know about the recipient's current status, and suggests catching up this week if available."}

- Tone : Output: {'Tone': 'Informal'}
  
- Reply : Output: {'subject': 'Re: Catching up', 'reply': "Hey there! Good to hear from you! Things have been pretty busy, but I'd love to catch up as well. Let's find a time that works for both of us this week. Looking forward to it!"}

# Challenges Faced
Handling invalid JSON responses from the LLM
Making reply tone match email tone
Improving prompt engineering for better classification

# Improvements Implemented
Strict JSON formatting
Tone-aware reply generation
Input text cleaning
Better prompt engineering
