```python
Generic_UNet(
  (conv_blocks_localization): ModuleList(
    (0): Sequential(
      (0): StackedConvLayers(
        (blocks): Sequential(
          (0): ConvDropoutNormNonlin(
            (conv): Conv3d(640, 320, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
            (instnorm): InstanceNorm3d(320, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
            (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
          )
        )
      )
      (1): StackedConvLayers(
        (blocks): Sequential(
          (0): ConvDropoutNormNonlin(
            (conv): Conv3d(320, 320, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
            (instnorm): InstanceNorm3d(320, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
            (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
          )
        )
      )
    )
    (1): Sequential(
      (0): StackedConvLayers(
        (blocks): Sequential(
          (0): ConvDropoutNormNonlin(
            (conv): Conv3d(512, 256, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
            (instnorm): InstanceNorm3d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
            (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
          )
        )
      )
      (1): StackedConvLayers(
        (blocks): Sequential(
          (0): ConvDropoutNormNonlin(
            (conv): Conv3d(256, 256, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
            (instnorm): InstanceNorm3d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
            (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
          )
        )
      )
    )
    (2): Sequential(
      (0): StackedConvLayers(
        (blocks): Sequential(
          (0): ConvDropoutNormNonlin(
            (conv): Conv3d(256, 128, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
            (instnorm): InstanceNorm3d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
            (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
          )
        )
      )
      (1): StackedConvLayers(
        (blocks): Sequential(
          (0): ConvDropoutNormNonlin(
            (conv): Conv3d(128, 128, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
            (instnorm): InstanceNorm3d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
            (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
          )
        )
      )
    )
    (3): Sequential(
      (0): StackedConvLayers(
        (blocks): Sequential(
          (0): ConvDropoutNormNonlin(
            (conv): Conv3d(128, 64, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
            (instnorm): InstanceNorm3d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
            (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
          )
        )
      )
      (1): StackedConvLayers(
        (blocks): Sequential(
          (0): ConvDropoutNormNonlin(
            (conv): Conv3d(64, 64, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
            (instnorm): InstanceNorm3d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
            (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
          )
        )
      )
    )
    (4): Sequential(
      (0): StackedConvLayers(
        (blocks): Sequential(
          (0): ConvDropoutNormNonlin(
            (conv): Conv3d(64, 32, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
            (instnorm): InstanceNorm3d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
            (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
          )
        )
      )
      (1): StackedConvLayers(
        (blocks): Sequential(
          (0): ConvDropoutNormNonlin(
            (conv): Conv3d(32, 32, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
            (instnorm): InstanceNorm3d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
            (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
          )
        )
      )
    )
  )
  (conv_blocks_context): ModuleList(
    (0): StackedConvLayers(
      (blocks): Sequential(
        (0): ConvDropoutNormNonlin(
          (conv): Conv3d(1, 32, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
          (instnorm): InstanceNorm3d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
          (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
        )
        (1): ConvDropoutNormNonlin(
          (conv): Conv3d(32, 32, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
          (instnorm): InstanceNorm3d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
          (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
        )
      )
    )
    (1): StackedConvLayers(
      (blocks): Sequential(
        (0): ConvDropoutNormNonlin(
          (conv): Conv3d(32, 64, kernel_size=[3, 3, 3], stride=[2, 2, 2], padding=[1, 1, 1])
          (instnorm): InstanceNorm3d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
          (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
        )
        (1): ConvDropoutNormNonlin(
          (conv): Conv3d(64, 64, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
          (instnorm): InstanceNorm3d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
          (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
        )
      )
    )
    (2): StackedConvLayers(
      (blocks): Sequential(
        (0): ConvDropoutNormNonlin(
          (conv): Conv3d(64, 128, kernel_size=[3, 3, 3], stride=[2, 2, 2], padding=[1, 1, 1])
          (instnorm): InstanceNorm3d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
          (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
        )
        (1): ConvDropoutNormNonlin(
          (conv): Conv3d(128, 128, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
          (instnorm): InstanceNorm3d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
          (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
        )
      )
    )
    (3): StackedConvLayers(
      (blocks): Sequential(
        (0): ConvDropoutNormNonlin(
          (conv): Conv3d(128, 256, kernel_size=[3, 3, 3], stride=[2, 2, 2], padding=[1, 1, 1])
          (instnorm): InstanceNorm3d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
          (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
        )
        (1): ConvDropoutNormNonlin(
          (conv): Conv3d(256, 256, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
          (instnorm): InstanceNorm3d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
          (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
        )
      )
    )
    (4): StackedConvLayers(
      (blocks): Sequential(
        (0): ConvDropoutNormNonlin(
          (conv): Conv3d(256, 320, kernel_size=[3, 3, 3], stride=[2, 2, 2], padding=[1, 1, 1])
          (instnorm): InstanceNorm3d(320, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
          (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
        )
        (1): ConvDropoutNormNonlin(
          (conv): Conv3d(320, 320, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
          (instnorm): InstanceNorm3d(320, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
          (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
        )
      )
    )
    (5): Sequential(
      (0): StackedConvLayers(
        (blocks): Sequential(
          (0): ConvDropoutNormNonlin(
            (conv): Conv3d(320, 320, kernel_size=[3, 3, 3], stride=[1, 2, 2], padding=[1, 1, 1])
            (instnorm): InstanceNorm3d(320, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
            (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
          )
        )
      )
      (1): StackedConvLayers(
        (blocks): Sequential(
          (0): ConvDropoutNormNonlin(
            (conv): Conv3d(320, 320, kernel_size=[3, 3, 3], stride=(1, 1, 1), padding=[1, 1, 1])
            (instnorm): InstanceNorm3d(320, eps=1e-05, momentum=0.1, affine=True, track_running_stats=False)
            (lrelu): LeakyReLU(negative_slope=0.01, inplace=True)
          )
        )
      )
    )
  )
  (td): ModuleList()
  (tu): ModuleList(
    (0): ConvTranspose3d(320, 320, kernel_size=[1, 2, 2], stride=[1, 2, 2], bias=False)
    (1): ConvTranspose3d(320, 256, kernel_size=[2, 2, 2], stride=[2, 2, 2], bias=False)
    (2): ConvTranspose3d(256, 128, kernel_size=[2, 2, 2], stride=[2, 2, 2], bias=False)
    (3): ConvTranspose3d(128, 64, kernel_size=[2, 2, 2], stride=[2, 2, 2], bias=False)
    (4): ConvTranspose3d(64, 32, kernel_size=[2, 2, 2], stride=[2, 2, 2], bias=False)
  )
  (seg_outputs): ModuleList(
    (0): Conv3d(320, 3, kernel_size=(1, 1, 1), stride=(1, 1, 1), bias=False)
    (1): Conv3d(256, 3, kernel_size=(1, 1, 1), stride=(1, 1, 1), bias=False)
    (2): Conv3d(128, 3, kernel_size=(1, 1, 1), stride=(1, 1, 1), bias=False)
    (3): Conv3d(64, 3, kernel_size=(1, 1, 1), stride=(1, 1, 1), bias=False)
    (4): Conv3d(32, 3, kernel_size=(1, 1, 1), stride=(1, 1, 1), bias=False)
  )
)
```

