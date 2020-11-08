#!/bin/bash

agent=hminimax2.py
echo -e "Using $agent\n"

echo -e "small/dumby"
python run.py --layout small_adv --agentfile $agent --ghostagent dumby
echo -e "\nsmall/greedy"
python run.py --layout small_adv --agentfile $agent --ghostagent greedy
echo -e "\nsmall/smarty"
python run.py --layout small_adv --agentfile $agent --ghostagent smarty
echo -e "\nmedium/dumby"
python run.py --layout medium_adv --agentfile $agent --ghostagent dumby
echo -e "\nmedium/greedy"
python run.py --layout medium_adv --agentfile $agent --ghostagent greedy
echo -e "\nmedium/smarty"
python run.py --layout medium_adv --agentfile $agent --ghostagent smarty
echo -e "\nlarge/dumby"
python run.py --layout large_adv --agentfile $agent --ghostagent dumby
echo -e "\nlarge/greedy"
python run.py --layout large_adv --agentfile $agent --ghostagent greedy
echo -e "\nlarge/smarty"
python run.py --layout large_adv --agentfile $agent --ghostagent smarty
