#!/bin/bash
paddle train --job=test \
             --use_gpu=1/0 \ 
             --config=network_config \
             --trainer_count=COUNT \ 
             --init_model_path=paddle-uci-train