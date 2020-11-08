#!/bin/bash

layout=large_adv

agent=hminimax0.py
echo -e "Using $agent\n"

echo -e "\n$agent/large/dumby"
python run.py --layout $layout --agentfile $agent --ghostagent dumby
echo -e "\n$agent/large/greedy"
python run.py --layout $layout --agentfile $agent --ghostagent greedy
echo -e "\n$agent/large/smarty"
python run.py --layout $layout --agentfile $agent --ghostagent smarty

agent=hminimax1.py
echo -e "\nUsing $agent\n"

echo -e "\n$agent/large/dumby"
python run.py --layout $layout --agentfile $agent --ghostagent dumby
echo -e "\n$agent/large/greedy"
python run.py --layout $layout --agentfile $agent --ghostagent greedy
echo -e "\n$agent/large/smarty"
python run.py --layout $layout --agentfile $agent --ghostagent smarty

agent=hminimax2.py
echo -e "\nUsing $agent\n"

echo -e "$agent/large/dumby"
python run.py --layout $layout --agentfile $agent --ghostagent dumby
echo -e "\n$agent/large/greedy"
python run.py --layout $layout --agentfile $agent --ghostagent greedy
echo -e "\n$agent/large/smarty"
python run.py --layout $layout --agentfile $agent --ghostagent smarty