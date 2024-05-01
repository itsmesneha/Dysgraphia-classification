import os
import shutil
import random

# Define source and destination directories
source_dir = 'resized-dataset'
train_dir = 'Final-data/train'
val_dir = 'Final-data/validation'
test_dir = 'Final-data/test'
train_split = 0.8
val_split = 0.1

# Create destination directories if they don't exist
os.makedirs(os.path.join(train_dir, 'potential-dysgraphia'), exist_ok=True)
os.makedirs(os.path.join(train_dir, 'low-potential-dysgraphia'), exist_ok=True)
os.makedirs(os.path.join(val_dir, 'potential-dysgraphia'), exist_ok=True)
os.makedirs(os.path.join(val_dir, 'low-potential-dysgraphia'), exist_ok=True)
os.makedirs(os.path.join(test_dir, 'potential-dysgraphia'), exist_ok=True)
os.makedirs(os.path.join(test_dir, 'low-potential-dysgraphia'), exist_ok=True)

# Perform train-validation-test split
for img in os.listdir(os.path.join(source_dir, 'Potential-resized')):
    rand_num = random.random()
    if rand_num < train_split:
        shutil.copy(os.path.join(source_dir, 'Potential-resized', img), os.path.join(train_dir, 'potential-dysgraphia', img))
    elif rand_num < train_split + val_split:
        shutil.copy(os.path.join(source_dir, 'Potential-resized', img), os.path.join(val_dir, 'potential-dysgraphia', img))
    else:
        shutil.copy(os.path.join(source_dir, 'Potential-resized', img), os.path.join(test_dir, 'potential-dysgraphia', img))

for img in os.listdir(os.path.join(source_dir, 'Low-Potential-resized')):
    rand_num = random.random()
    if rand_num < train_split:
        shutil.copy(os.path.join(source_dir, 'Low-Potential-resized', img), os.path.join(train_dir, 'low-potential-dysgraphia', img))
    elif rand_num < train_split + val_split:
        shutil.copy(os.path.join(source_dir, 'Low-Potential-resized', img), os.path.join(val_dir, 'low-potential-dysgraphia', img))
    else:
        shutil.copy(os.path.join(source_dir, 'Low-Potential-resized', img), os.path.join(test_dir, 'low-potential-dysgraphia', img))

print("Splitting into train-validation-test completed successfully.")
