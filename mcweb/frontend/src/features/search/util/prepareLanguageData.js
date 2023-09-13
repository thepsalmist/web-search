const colorArray = ['#2f2d2b', '#d24527', '#2f2d2b', '#d23716', '#f7a44e'];

export default function prepareLanguageData(languageData) {
  const series = [];
  languageData.forEach((queryData, i) => {
    series.push(
      {
        data: queryData.languages.map((l) => ({
          key: l.language, value: l.ratio * 100,
        })),
        name: 'Language',
        color: colorArray[i],
      },
    );
  });
  return series;
}

// series requirements for word cloud
// series={[{
//   data: data.languages.map((l) => ({
//     key: l.language, value: l.ratio * 100,
//   })),
//   name: 'Language',
//   color: '#2f2d2b',
// }]}
