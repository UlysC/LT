from datetime import datetime


defaultImageSrc = 'https://picsum.photos/2500/1500'
lorem = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis sapien massa, interdum at arcu eu, laoreet semper metus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras interdum, ipsum at maximus venenatis, justo libero egestas turpis, sit amet lobortis felis neque eu ipsum. Nulla id quam pretium, molestie erat ut, egestas massa. Ut in purus eget tortor efficitur vestibulum. Vivamus pulvinar interdum ipsum, sit amet ornare sem blandit at. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed nec nisl risus.

Etiam ut quam a justo pulvinar tempus eget sed nisl. Morbi lectus metus, porttitor vitae finibus nec, malesuada a augue. Vivamus tempor, nulla sed finibus aliquam, magna massa pretium justo, ac suscipit odio sem interdum nisl. In vitae justo feugiat, dapibus tellus a, commodo justo. Donec congue ornare arcu sit amet mollis. Nunc efficitur interdum finibus. Maecenas ac orci lacinia, scelerisque mi sed, varius lacus.

Mauris tristique ac odio eu dapibus. Etiam accumsan tempus posuere. Nunc mollis sapien velit, sit amet condimentum dui condimentum eget. Integer quam felis, imperdiet nec pulvinar non, commodo ac nunc. Suspendisse gravida ullamcorper libero nec euismod. Proin finibus neque quis velit dictum convallis. Vivamus placerat lacus nec libero euismod commodo. Cras at posuere orci, dapibus mollis neque. Pellentesque consequat, est non feugiat placerat, magna lorem consectetur erat, vitae cursus diam sem et arcu. Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras imperdiet ac arcu id mattis. Cras pulvinar tincidunt leo, in faucibus elit dignissim nec. Suspendisse tempor ut nibh nec consequat.

Nam et mauris et tortor varius ornare vitae nec tellus. Curabitur lobortis, leo ultricies sagittis cursus, mauris magna vulputate purus, in lobortis urna elit ac nisi. In venenatis dolor sed massa tristique, in sodales quam malesuada. Integer feugiat, magna et tempus maximus, purus orci accumsan ipsum, non ornare arcu sem quis lorem. Nulla sem mi, varius eu mi eu, iaculis rutrum eros. Fusce nisi nulla, dictum eu odio et, ornare vehicula ligula. Ut diam magna, faucibus at gravida vitae, malesuada non odio. Cras pharetra, erat ut pharetra bibendum, felis diam ultricies odio, vitae tincidunt sapien ligula vel sem. Sed a justo suscipit, facilisis orci sed, varius quam. Ut eu quam sed orci aliquet pretium id eu odio. Pellentesque imperdiet magna in nisi tempus aliquet. Pellentesque nec aliquet neque. Phasellus rutrum velit id urna pulvinar, ac tristique mi molestie.

Suspendisse ac aliquam quam. Morbi suscipit metus non tincidunt tempus. Morbi eros sem, ultricies id mattis vel, venenatis ac mi. Donec mollis nunc id nunc vehicula pharetra. Integer imperdiet nisi ligula, et aliquam magna porta nec. Nam efficitur, diam ac luctus pulvinar, metus quam lacinia tellus, vel bibendum erat dui vitae augue. In viverra, augue et fringilla scelerisque, nibh est dictum orci, eu mollis mi massa ut neque. Fusce risus leo, feugiat ac tincidunt ut, faucibus eget nisi. """

dataBaseInMemory = [
    {
        'id':1,
        'title': 'Article 1',
        'content': lorem,
        'image': {
            'alt': 'image 1',
            'src': defaultImageSrc,
        },
        'createdAt': datetime.today().strftime('%Y-%m-%d')
       },
    {
        'id':2,
        'title': 'Article 2',
        'content': lorem, 
        'image': {
            'alt': 'image 2',
            'src': 'https://picsum.photos/2400/1500',
        },
        'createdAt': datetime.today().strftime('%Y-%m-%d')
       },
    {
        'id':3,
        'title': 'Article 3',
        'content': lorem, 
        'image': {
            'alt': 'image 3',
            'src': 'https://picsum.photos/2400/1400',
        },
        'createdAt': datetime.today().strftime('%Y-%m-%d')
       },
]