from tools.infer import main, pre_trainer,do_work

if __name__ == '__main__':
    flags, cfg = main()
    trainer, flags = pre_trainer(flags, cfg)
    results, save_name = do_work(trainer, flags)
    print(results)
    print(save_name)
