import qtc.ext.unittest as ut
from backup.ext.path import bam_dir, sysequity_dir


class TestPath(ut.TestCase):
    def test_bam_dir(self):
        self.assertEqual(bam_dir(platform_system='Windows'),
                         '\\\\fountainhead\\bam')
        self.assertEqual(bam_dir(platform_system='Linux'),
                         '/bam')
        self.assertEqual(bam_dir('DataApi', 'config_shared', platform_system='Windows'),
                         '\\\\fountainhead\\bam\\DataApi\\config_shared')
        self.assertEqual(bam_dir('DataApi', 'config_shared', platform_system='Linux'),
                         '/bam/DataApi/config_shared')

    def sysequity_dir(self):
        self.assertEqual(sysequity_dir(platform_system='Windows'),
                         '\\\\aws-prod-nas\\team_sysequity')
        self.assertEqual(sysequity_dir(platform_system='Linux'),
                         '/bam/aws/prod/team_sysequity')
        self.assertEqual(sysequity_dir('Reports', 'PMs', platform_system='Windows'),
                         '\\\\aws-prod-nas\\team_sysequity\\Reports\\PMs')
        self.assertEqual(sysequity_dir('Reports', 'PMs', platform_system='Linux'),
                         '/bam/aws/prod/team_sysequity/Reports/PMs')


if __name__ == '__main__':
    ut.main()
