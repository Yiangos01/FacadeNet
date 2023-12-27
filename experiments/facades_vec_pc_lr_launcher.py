from .tmux_launcher import Options, TmuxLauncher


class Launcher(TmuxLauncher):
    def options(self):
        opt = Options()
        opt.set(

            dataroot="/media/yiangos/Urban_Enviroment_Understanding_Project/LSAA/facade_data_full/interactive_textures_sem/facades/",
            dataroot_sem="/media/yiangos/Urban_Enviroment_Understanding_Project/LSAA/facade_data_full/interactive_textures_sem/semantics/",
            dataroot_feats="/media/yiangos/Urban_Enviroment_Understanding_Project/LSAA/facade_data_full/interactive_textures_sem/vit_feats_4/",
            dataroot_depth="/media/yiangos/Urban_Enviroment_Understanding_Project/LSAA/facade_data_full/interactive_textures_sem/depth/",
            dataroot_h="/media/yiangos/Urban_Enviroment_Understanding_Project/LSAA/facade_data_full/interactive_textures_sem/horizontal_maps/",
            dataroot_v="/media/yiangos/Urban_Enviroment_Understanding_Project/LSAA/facade_data_full/interactive_textures_sem/vertical_maps/",
            train_split_dir="/media/yiangos/Urban_Enviroment_Understanding_Project/LSAA/facade_data_full/interactive_textures_sem/train_split.txt",
            eval_split_dir ="/media/yiangos/Urban_Enviroment_Understanding_Project/LSAA/facade_data_full/interactive_textures_sem/eval_split.txt",

            # dataroot="/lustreFS/data/vcg/yiangos/interactive_textures_sem/facades/",
            # dataroot_sem="/lustreFS/data/vcg/yiangos/interactive_textures_sem/vit_pc/",
            # dataroot_feats="/lustreFS/data/vcg/yiangos/interactive_textures_sem/vit_pc/vit_feats/",
            # dataroot_depth="/lustreFS/data/vcg/yiangos/interactive_textures_sem/depth/",
            # dataroot_h="/lustreFS/data/vcg/yiangos/interactive_textures_sem/horizontal_maps/",
            # dataroot_v="/lustreFS/data/vcg/yiangos/interactive_textures_sem/vertical_maps/",
            # train_split_dir="/lustreFS/data/vcg/yiangos/interactive_textures_sem/train_split.txt",
            # eval_split_dir="/lustreFS/data/vcg/yiangos/interactive_textures_sem/eval_split.txt",

            dataset_mode="imagefolder_va_depth_lr",
            num_gpus=1, batch_size=4,
            preprocess="resize_and_crop",
            nThreads=32,
            # scale the image such that the short side is |load_size|, and
            # crop a square window of |crop_size|.
            load_size=280, crop_size=256,
            display_freq=1600, print_freq=200,
            model='autoencoder_va_vec_lr', optimizer='autoencoder_va_vec_lr',
            lambda_L1=3,
            checkpoints_dir="./checkpoints",
            lambda_sel_L1=3
            # parser.add_argument('--model', type=str, default='swapping_autoencoder', help='which model to use')
            # parser.add_argument('--optimizer', type=str, default='swapping_autoencoder', help='which model to use')
        ),

        return [
            opt.specify(
                name="facadenet",
            ),
        ]

    def train_options(self):
        common_options = self.options()
        return [opt.specify(
            continue_train=False,
            evaluation_metrics="va_visualization_vec",
            evaluation_freq=25000,
        ) for opt in common_options]

    def test_options_fid(self):
        return []

    def test_options(self):
        common_options = self.options()

        return [opt.tag("fig4").specify(
            phase='test',
            num_gpus=1,
            batch_size=1,
            dataroot="/media/yiangos/Urban_Enviroment_Understanding_Project/LSAA/facade_data_full/interactive_textures_sem/facades/",
            dataroot_sem="/media/yiangos/Urban_Enviroment_Understanding_Project/LSAA/facade_data_full/interactive_textures_sem/vit_pc/",
            dataroot_depth="/media/yiangos/Urban_Enviroment_Understanding_Project/LSAA/facade_data_full/interactive_textures_sem/depth/",
            dataroot_h="/media/yiangos/Urban_Enviroment_Understanding_Project/LSAA/facade_data_full/interactive_textures_sem/horizontal_maps/",
            dataroot_v="/media/yiangos/Urban_Enviroment_Understanding_Project/LSAA/facade_data_full/interactive_textures_sem/vertical_maps/",
            train_split_dir="/media/yiangos/Urban_Enviroment_Understanding_Project/LSAA/facade_data_full/interactive_textures_sem/train_split.txt",
            eval_split_dir ="/media/yiangos/Urban_Enviroment_Understanding_Project/LSAA/facade_data_full/interactive_textures_sem/eval_split.txt",
            dataset_mode="imagefolder_va",
            preprocess="resize",
            evaluation_metrics="va_visualization_vec",
        ) for opt in common_options]

