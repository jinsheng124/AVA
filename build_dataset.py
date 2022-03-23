from datasets.ava_dataset import Ava
import torch
from cfg import parser
args  = parser.parse_args()
cfg   = parser.load_config(args)
train_dataset = Ava(cfg, split='train',only_detection=False)
test_dataset = Ava(cfg, split='val',only_detection=False)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=cfg.TRAIN.BATCH_SIZE, shuffle=True,
                                           num_workers=cfg.DATA_LOADER.NUM_WORKERS, drop_last=True, pin_memory=True)

test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=cfg.TRAIN.BATCH_SIZE, shuffle=False,
                                          num_workers=cfg.DATA_LOADER.NUM_WORKERS, drop_last=False, pin_memory=True)
if __name__=="__main__":
    for batch_idx, batch in enumerate(train_loader):
        data = batch['clip'].cuda()
        target = {'cls': batch['cls'], 'boxes': batch['boxes']}
        print(data.shape)
        print(target)
        print("----------------")